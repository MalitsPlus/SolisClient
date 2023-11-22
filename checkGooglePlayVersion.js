import gplay from "google-play-scraper"
import { mkdirSync, writeFileSync } from "fs"

async function main() {
  const appInfo = await gplay.app({ appId: 'game.qualiarts.idolypride' })
  mkdirSync("cache", { recursive: true })
  writeFileSync("cache/appversion", appInfo.version, () => { })
}

main()
