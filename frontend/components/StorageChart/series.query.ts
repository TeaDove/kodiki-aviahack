import { useQuery, useQueryClient } from "@tanstack/react-query";
import { getSeries } from "../../api/api";
import { Series } from "./series.model";
import { ScaleValues } from "./StorageChart";

const keys = {
  all: ['series'],
  byScale: (scale?: string) => [...keys.all, scale],
} as const;

const useCashedSeriesInitialData = (id: string) => {
  const queryClient = useQueryClient();
  return {
    initialData() {
      return queryClient
        .getQueryData<Series[]>(keys.all)
        ?.find((t) => t.id === id);
    },
  }
}

const fromScale = {
  daily: {
    delta: 30 * 2,
    precisionDays: 1,
  },
  monthly: {
    delta: 30 * 12 * 2,
    precisionDays: 30,
  },
  yearly: {
    delta: 365 * 3 * 2,
    precisionDays: 365,
  },
}

const useSeries = (scale: ScaleValues = 'daily') => {
  return useQuery(keys.byScale(scale), () => getSeries(fromScale[scale].delta, fromScale[scale].precisionDays));
}

export {
  keys,
  useCashedSeriesInitialData,
  useSeries,
}
