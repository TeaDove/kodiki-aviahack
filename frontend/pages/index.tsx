import type { NextPage } from 'next';
import { useSeries } from '../components/StorageChart/series.query';
import CardChart from '../components/ChartCard/ChartCard';
import colors from 'tailwindcss/colors';
import { ScaleValues } from '../components/StorageChart/StorageChart';
import { useState } from 'react';

const Home: NextPage = () => {
  const [keepingScale, setKeepingScale] = useState<ScaleValues>('daily');
  const [receivingScale, setReceivingScale] = useState<ScaleValues>('daily');

  const keepingData = useSeries(keepingScale).data?.filter(
    ({ id }) => id === 'keeping'
  );
  const receivingData = useSeries(receivingScale).data?.filter(
    ({ id }) => id === 'receiving'
  );

  return (
    <>
      <div className="w-full">
        <CardChart
          title="Хранение"
          data={keepingData}
          onScaleChange={setKeepingScale}
        />
      </div>
      <div className="mt-10 w-full">
        <CardChart
          title="Обработка"
          data={receivingData}
          color={colors.orange[600]}
          onScaleChange={setReceivingScale}
        />
      </div>
    </>
  );
};

export default Home;
