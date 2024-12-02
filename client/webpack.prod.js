const { merge } = require('webpack-merge');
const webpackConfig = require('./webpack.config.js');

module.exports = (merge(webpackConfig, {
    mode: 'production',
    output: {
        publicPath: './dist', 
        clean: true,
    }
}));