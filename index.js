// include dependencies
const express = require("express");
const { createProxyMiddleware } = require("http-proxy-middleware");

// proxy middleware options
/** @type {import('http-proxy-middleware/dist/types').Options} */
const options = {
  changeOrigin: true,
  target: "http://localhost:5000",
  logLevel: "debug",
  onProxyRes: (proxyRes, req, res) => {
    // log original request and proxied request info
    const exchange = `[DEBUG] ${req.method} ${req.path} -> ${proxyRes.req.protocol}//${proxyRes.req.host}${proxyRes.req.path} [${proxyRes.statusCode}]`;
    console.log(exchange); // [DEBUG] GET / -> http://www.example.com [200]
  },
  onError: (err, req, res) => console.log({ err }),
};

// create the proxy (without context)
const exampleProxy = createProxyMiddleware(options);

// mount `exampleProxy` in web server
const app = express();
app.use("/api", exampleProxy);
app.listen(3000);
