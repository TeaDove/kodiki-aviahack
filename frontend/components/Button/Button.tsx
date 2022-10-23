type ButtonProps = {
  onClick: () => void;
  active?: boolean;
  children: React.ReactNode;
};

const Button: React.FC<ButtonProps> = ({ active, onClick, children }) => {
  return (
    <button
      className={`rounded-lg bg-gray-100 py-3 px-4 font-medium transition-colors hover:bg-gray-200 active:bg-gray-300 ${
        active && 'bg-red-600 text-white hover:bg-red-700 active:bg-red-800'
      } ${!active && 'text-gray-700'}`}
      onClick={onClick}
    >
      {children}
    </button>
  );
};

export default Button;
