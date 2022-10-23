import Navbar from '../Navbar/Navbar';

type LayoutProps = {
  children: React.ReactNode;
};

const Layout: React.FC<LayoutProps> = ({ children }) => {
  return (
    <div className="flex min-h-screen justify-center bg-gray-200 text-gray-700">
      <Navbar />
      <main className="flex w-full flex-col items-center p-6">{children}</main>
    </div>
  );
};

export default Layout;
