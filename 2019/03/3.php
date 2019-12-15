<?php
  error_reporting(E_ALL);
  ini_set('display_errors', 1);

  class Segment {
    public $orientation;
    public $direction;
    public $low;
    public $high;

    static public function fromInstruction($start, $instruction) {
      $direction = substr($instruction, 0, 1);
      $amount = intval(substr($instruction, 1));
      $delta = ['R' => [ 1,  0],
                'L' => [-1,  0],
                'U' => [ 0,  1],
                'D' => [ 0, -1]][$direction];
      $end[0] = $start[0] + $amount * $delta[0];
      $end[1] = $start[1] + $amount * $delta[1];
      $orientation = ['L' => 0, 'R' => 0, 'U' => 1, 'D' => 1][$direction];
      $position = $start[1 - $orientation];

      return [
        'segment' => new Segment(
          $orientation,
          $position,
          $start[$orientation],
          $end[$orientation]
        ),
        'end' => $end
      ];
    }
    public function __construct($orientation, $position, $source, $destination) {
      if ($source < $destination) {
        $this->low = $source;
        $this->high = $destination;
        $this->direction = 1;
      }
      else {
        $this->low = $destination;
        $this->high = $source;
        $this->direction = -1;
      }
      assert(is_int($this->low) && is_int($this->high));
      assert($this->low <= $this->high);
      $this->orientation = $orientation;
      $this->position = $position;
    }
    public function intersect($other) {
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
             return [$other->position, $this->position];
           }
           return [$this->position, $other->position];
        }
      }
      return NULL;
    }
    public function length() {
      return $this->high - $this->low;
    }
    public function pointLocation($point) {
      if ($point[1 - $this->orientation] != $this->position) {
        return NULL;
      }
      $location = $point[$this->orientation];
      if ($location < $this->low || $location > $this->high) {
        return NULL;
      }
      if ($this->direction == 1) {
        return $location - $this->low;
      }
      else {
        return $this->high - $location;
      }
    }
    public function pointNearestOrigin() {
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
        'end' => $location
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
  $bestDelay = INF;

  $delay0 = 0;
  foreach ($segments[0] as $segment0) {
    $delay1 = 0;
    foreach ($segments[1] as $segment1) {
      $candidate = $segment0->intersect($segment1);
      if ($candidate instanceof Segment) {
        $candidate = $candidate->pointNearestOrigin();
      }
      if (!is_null($candidate)) {
        $candidateDistance = manhattan($candidate);
        if ($candidateDistance > 0) {
          $bestDistance = min($bestDistance, $candidateDistance);
        }
        $candidateDelay = $delay0 + $segment0->pointLocation($candidate)
                        + $delay1 + $segment1->pointLocation($candidate);
        if ($candidateDelay > 0) {
          $bestDelay = min($bestDelay, $candidateDelay);
        }
      }
      $delay1 += $segment1->length();
    }
    $delay0 += $segment0->length();
  }

  echo "Best distance: $bestDistance\n";
  echo "Best delay: $bestDelay\n";
?>
