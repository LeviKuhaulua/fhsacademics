import { merge } from 'webpack-merge';
import webpackConfig from './webpack.config.js';


module.exports(merge(webpackConfig, {
    mode: 'production',
}));