const path = require('path');
const { merge } = require('webpack-merge');
const webpackConfig = require('./webpack.config.js');


module.exports(merge(webpackConfig, {
    mode: 'development', 
}));