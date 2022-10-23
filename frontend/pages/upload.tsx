import type { NextPage } from 'next';
import { useSeries } from '../components/StorageChart/series.query';
import { ScaleValues } from '../components/StorageChart/StorageChart';
import { useState } from 'react';
import Card from '../components/Card/Card';
import FileUpload from '../components/FileUpload/FileUpload';
import Button from '../components/Button/Button';

const Upload: NextPage = () => {
  const [keepingScale, setKeepingScale] = useState<ScaleValues>('daily');

  const keepingData = useSeries(keepingScale).data?.filter(
    ({ id }) => id === 'keeping'
  );

  return (
    <>
      <div className="w-full">
        <Card title="Загрузка данных">
          <p className="mt-2 text-slate-500">
            Для того, чтобы загрузить новые данные для расчёта, вставьте в форму
            ниже специально подготовленный csv файл
          </p>
          <div className="mt-6">
            <FileUpload />
          </div>
          <div className="mt-6">
            <Button active onClick={() => {}}>
              Загрузить
            </Button>
          </div>
        </Card>
      </div>
    </>
  );
};

export default Upload;
