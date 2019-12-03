<?php
  error_reporting(E_ALL);
  ini_set('display_errors', 1);

  class Segment {
    public $orientation;
    public $low;
    public $high;

    static function fromInstruction($source, $instruction) {
      $direction = substr($instruction, 0, 1);
      $amount = intval(substr($instruction, 1));
      $delta = ['R' => [ 1,  0],
                'L' => [-1,  0],
                'U' => [ 0,  1],
                'D' => [ 0, -1]][$direction];
      $destination[0] = $source[0] + $amount * $delta[0];
      $destination[1] = $source[1] + $amount * $delta[1];
      $orientation = ['L' => 0, 'R' => 0, 'U' => 1, 'D' => 1][$direction];
      $position = $source[1 - $orientation];
      $low = min($source[$orientation], $destination[$orientation]);
      $high = max($source[$orientation], $destination[$orientation]);

      return [
        'segment' => new Segment($orientation, $position, $low, $high),
        'destination' => $destination
      ];
    }
    function __construct($orientation, $position, $low, $high) {
      assert($low <= $high);
      $this->orientation = $orientation;
      $this->position = $position;
      $this->low = $low;
      $this->high = $high;
    }
    function intersect($other) {
      if ($this->orientation == $other->orientation) {
        if ($this->position == $other->position) {
          $low = max($this->low, $other->low);
          $high = min($this->high, $other->high);
          if ($low <= $high) {
            return new Segment(
              $this->orientation, $this->position, $low, $high
            );
          }
        }
      }
      else {
        if ($this->low <= $other->position && $other->position <= $this->high
         && $other->low <= $this->position && $this->position <= $other->high) {
           if ($this->orientation == 0) {
             return [$this->position, $other->position];
           }
           return [$other->position, $this->position];
        }
      }
      return NULL;
    }
    function pointNearestOrigin() {
      if ($this->low <= 0 && $this->high >= 0) {
        $bestCoordinate = 0;
      }
      else {
        if ($this->low < 0) {
          $bestCoordinate = max($this->low, $this->high);
        }
        else {
          $bestCoordinate = min($this->low, $this->high);
        }
      }
      if ($this->orientation == 0) {
        return [$bestCoordinate, $this->position];
      }
      return [$this->position, $bestCoordinate];
    }
  }

  function manhattan($point) {
    return abs($point[0]) + abs($point[1]);
  }

  function segments($path) {
    $segments = [];
    $location = [0, 0];
    foreach ($path as $instruction) {
      [
        'segment' => $segment,
        'destination' => $location
      ] = Segment::fromInstruction($location, $instruction);
      $segments[] = $segment;
    }
    return $segments;
  }

  $paths = file('3.txt');
  $paths[0] = explode(',', $paths[0]);
  $paths[1] = explode(',', $paths[1]);

  $segments = [
    segments($paths[0]),
    segments($paths[1])
  ];

  $bestDistance = INF;

  foreach ($segments[0] as $segment0) {
    foreach ($segments[1] as $segment1) {
      $candidate = $segment0->intersect($segment1);
      if ($candidate instanceof Segment) {
        $candidate = $candidate->pointNearestOrigin();
      }
      if (is_null($candidate)) {
        continue;
      }
      $candidateDistance = manhattan($candidate);
      if ($candidateDistance > 0) {
        $bestDistance = min($bestDistance, $candidateDistance);
      }
    }
  }

  echo "$bestDistance\n";
?>
