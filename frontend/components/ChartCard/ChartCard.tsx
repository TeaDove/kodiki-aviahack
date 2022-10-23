import { useState } from 'react';
import Button from '../Button/Button';
import Card from '../Card/Card';
import { Series } from '../StorageChart/series.model';
import StorageChart, { ScaleValues } from '../StorageChart/StorageChart';

type CardChartProps = {
  title: string;
  data?: Series[];
  color?: string;
  onScaleChange?: (value: ScaleValues) => void;
};

const CardChart: React.FC<CardChartProps> = ({
  title,
  data,
  color,
  onScaleChange,
}) => {
  const [scale, setScale] = useState<ScaleValues>('daily');

  const handleScaleChange = (value: ScaleValues) => {
    setScale(value);
    onScaleChange?.(value);
  };

  return (
    <Card title={title}>
      <div className="h-96 w-full">
        {data ? (
          <StorageChart data={data} scale={scale} color={color} />
        ) : (
          <div className="flex h-full items-center justify-center text-lg">
            Loading...
          </div>
        )}
      </div>
      <div className="flex p-4">
        <div>
          <Button
            active={scale === 'daily'}
            onClick={() => handleScaleChange('daily')}
          >
            По дням
          </Button>
        </div>
        <div className="ml-3">
          <Button
            active={scale === 'monthly'}
            onClick={() => handleScaleChange('monthly')}
          >
            По месяцам
          </Button>
        </div>
        <div className="ml-3">
          <Button
            active={scale === 'yearly'}
            onClick={() => handleScaleChange('yearly')}
          >
            По годам
          </Button>
        </div>
      </div>
    </Card>
  );
};

export default CardChart;
