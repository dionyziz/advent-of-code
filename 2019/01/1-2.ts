import * as fs from "promisified-fs"
import * as R from "ramda"

async function input() {
  let lines =
    (await fs.readFile('input.txt')).toString('ascii')
    .split('\n').slice(0, -1)
  return lines.map((x: string) => parseInt(x, 10))
}

function fuelRequiredForModule(mass: number) {
  function addExtraFuel(masses: number[]): number[] {
    return R.append(R.max(0, Math.floor(R.last(masses) / 3) - 2), masses)
  }

  let seq =
    R.until(
      R.compose(R.equals(0), R.last),
      addExtraFuel,
      [mass]
    )

  return R.sum(R.tail(seq))
}

function solve(modules: number[]) {
  return R.sum(modules.map(fuelRequiredForModule))
}

(async () => {
  console.log(solve(await input()))
})()
