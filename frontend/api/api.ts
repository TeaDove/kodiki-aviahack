import moment from "moment";
import { Series } from "../components/StorageChart/series.model";
import { apiBasePath, paths } from "../config"

export async function getSeries(delta = 365, precisionDays = 1): Promise<Series[]> {
  const from = moment().subtract(Math.floor(delta / 3), 'day').format('YYYY-MM-DD');
  const to = moment().add(Math.floor(delta * 2 / 3), 'day').format('YYYY-MM-DD');
  const series: Series[] = (await (await fetch(new URL(`${paths.series}?precisionDays=${precisionDays}&from=${from}&to=${to}`, apiBasePath))).json()).series;
  return series;
}
