import { linearGradientDef } from '@nivo/core';
import { ResponsiveLine } from '@nivo/line';
import colors from 'tailwindcss/colors';
import { Series } from './series.model';

type StorageChartProps = {
  data: Series[];
  scale?: ScaleValues;
  color?: string;
};

export type ScaleValues = 'daily' | 'monthly' | 'yearly';

const scaleToMonths = {
  daily: 1,
  monthly: 30,
  yearly: 365,
};

const upperScale = {
  daily: 30,
  monthly: 12 * 30,
  yearly: 3 * 365,
};

const formatScale = {
  daily: '%b %d',
  monthly: '%b',
  yearly: '%Y',
};

const StorageChart: React.FC<StorageChartProps> = ({
  data,
  scale = 'daily',
  color,
}) => {
  return (
    <ResponsiveLine
      data={data}
      margin={{ top: 50, right: 0, bottom: 50, left: 60 }}
      xScale={{
        type: 'time',
        format: '%Y-%m-%d',
        precision: 'day',
      }}
      xFormat="time:%Y-%m-%d"
      yScale={{
        type: 'linear',
        reverse: false,
      }}
      yFormat={(value) => `${Number(value).toFixed(2)}m³`}
      markers={[
        {
          axis: 'x',
          value: new Date(),
          lineStyle: {
            stroke: colors.blue[500],
            strokeWidth: 2,
            strokeDasharray: 6,
          },
          legend: 'Текущая дата',
          textStyle: {
            fill: colors.zinc[700],
            transform: 'translate(20px, -15px)',
          },
          legendPosition: 'top',
        },
      ]}
      enableSlices="x"
      enableArea={data.length === 1}
      areaOpacity={0.3}
      axisBottom={{
        tickSize: 0,
        tickPadding: 10,
        tickValues: `every ${
          scale === 'daily' ? scaleToMonths[scale] * 3 : scaleToMonths[scale]
        } days`,
        format: formatScale[scale],
      }}
      axisLeft={{
        tickSize: 0,
        tickPadding: 10,
        tickRotation: 0,
        legend: 'объем м³',
        legendOffset: -48,
        legendPosition: 'middle',
      }}
      pointSize={10}
      pointColor={{ theme: 'background' }}
      pointBorderWidth={2}
      pointBorderColor={{ from: 'serieColor' }}
      pointLabelYOffset={-12}
      useMesh={true}
      defs={[
        linearGradientDef('gradientA', [
          { offset: 0, color: 'inherit' },
          { offset: 100, color: 'inherit', opacity: 0 },
        ]),
      ]}
      fill={[{ match: '*', id: 'gradientA' }]}
      lineWidth={3}
      curve="cardinal"
      colors={
        color
          ? [color]
          : [colors.red[600], colors.blue[600], colors.orange[600]]
      }
      sliceTooltip={({ slice }) => (
        <div className="min-w-[170px] rounded-xl border border-zinc-200 bg-white p-4 shadow-lg">
          <div>
            <span className="font-bold">{slice.points[0].data.xFormatted}</span>
          </div>
          {slice.points.map(
            ({ data: { yFormatted }, id, serieId, serieColor }) => (
              <div className="flex items-center" key={id}>
                <div
                  className="mr-2 h-2.5 w-2.5 rounded-full"
                  style={{ backgroundColor: serieColor }}
                ></div>
                <div className="flex w-full justify-between">
                  <div>{serieId}</div>
                  <div className="ml-2">
                    <span className="text-right font-bold">{yFormatted}</span>
                  </div>
                </div>
              </div>
            )
          )}
        </div>
      )}
      theme={{
        textColor: colors.zinc[700],
        tooltip: {
          container: {
            borderRadius: 8,
          },
        },
        fontSize: 14,
        grid: {
          line: {
            stroke: colors.zinc[200],
            strokeWidth: 1,
          },
        },
        crosshair: {
          line: {
            stroke: colors.zinc[600],
            strokeWidth: 2,
          },
        },
      }}
    />
  );
};

export default StorageChart;
