const path = require('path');
const fs = require('node:fs');

// Gets entry points for webpack. 
function getEntries(folder) {
    const files = fs.readdirSync(folder);
    const entries = {};

    for (const file of files) {
        try {
            entries[`${file.toString().split('.')[0]}`] = `${folder}/${file.toString()}`;
        } catch (e) {
            console.error(e);
        }
    }
    return entries;
}


module.exports = {
    entry: getEntries('./src/pages'),
    output: {
        filename: '[name].js',
        path: path.resolve(__dirname, '..', 'public', 'dist'),
        assetModuleFilename: 'assets/[name][ext][query]',
    }, 
    resolve: {
        extensions: ['.tsx', '.ts', '.jsx', '.js'],
    }, 
    module: {
        rules: [
            {
                test: /\.(ts|tsx)$/,
                exclude: /node_modules/,
                use: ['ts-loader'],  
            }, 
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader', 
                    options: {
                        presets: ['@babel/preset-env', '@babel/preset-react'], 
                    },
                }
            }, 
            {
                test:/\.(png|jpe?g|svg|webp)$/,
                type: 'asset/resource',
            },
            {
                test:/\.css$/,
                use: ['style-loader', 'css-loader'], 
            }
        ]
    }
}