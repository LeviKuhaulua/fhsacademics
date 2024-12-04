const path = require('path');
const { merge } = require('webpack-merge');
const webpackConfig = require('./webpack.config.js');


module.exports = (merge(webpackConfig, {
    mode: 'development', 
    output: {
        // tells Webpack where to look for generated bundles in dev server
        publicPath: '/dist/', 
    },
    devServer: {
        open: true, 
        port: 5500,
        // disabling Hot Module Replacement so that liveReload can be enabled 
        hot: false, 
        liveReload: true,
        static: {
            directory: path.join(__dirname, '..', 'public'),
        },
        // est. proxy so that it allows us to access API from frontend
        proxy: [
            {
                context: ['/announcements'], 
                target: 'http://localhost:8000/',
            }
        ], 
    },
    
    
    
}));