import * as fs from "promisified-fs"
import * as R from "ramda"

async function input() {
  let lines =
    (await fs.readFile('input.txt')).toString('ascii')
    .split('\n').slice(0, -1)
  return lines.map(x => parseInt(x, 10))
}
function solve(modules) {
  return R.sum(modules.map(mass => Math.floor(mass / 3) - 2))
}

(async () => {
  console.log(solve(await input()))
})()
