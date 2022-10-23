type CardProps = {
  title: string;
  children: React.ReactNode;
};

const Card: React.FC<CardProps> = ({ children, title }) => {
  return (
    <div className="flex w-full flex-col rounded-2xl border border-zinc-300 bg-white p-6 shadow-sm">
      <h2 className="text-4xl">
        <strong>{title}</strong>
      </h2>
      {children}
    </div>
  );
};

export default Card;
