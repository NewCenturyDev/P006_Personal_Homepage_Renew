module.exports = {
    outputDir: '../backend/src/view',
	publicPath: process.env.NODE_ENV === 'production'
    ? './'
    : '/'
}