import '../styles/globals.css';
import type { AppProps } from 'next/app';
import Head from 'next/head';
import { CssBaseline, StyledEngineProvider } from '@mui/material';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { ReactQueryDevtools } from '@tanstack/react-query-devtools';
import Layout from '../components/Layout/Layout';

const queryClient = new QueryClient();

function App({ Component, pageProps }: AppProps) {
  return (
    <QueryClientProvider client={queryClient}>
      <StyledEngineProvider injectFirst>
        <CssBaseline>
          <Head>
            <title>Aviahack App</title>
            <meta
              name="viewport"
              content="initial-scale=1, width=device-width"
            />
            <link rel="stylesheet" href="https://rsms.me/inter/inter.css" />
            <link rel="stylesheet" href="fonts.css" />
            <link rel="icon" href="favicon.ico" />
          </Head>
          <Layout>
            <Component {...pageProps} />
          </Layout>
          <ReactQueryDevtools />
        </CssBaseline>
      </StyledEngineProvider>
    </QueryClientProvider>
  );
}

export default App;
