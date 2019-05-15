const fs = require('fs')
const chalk = require('chalk')

const addProduct = (num, name, imgPath) => {
	const products = loadProducts()

	const duplicates = products.find((product) => product.name === name)

	if (!duplicates) {
		products.push({
			num: num,
			name: name,
			imgPath: imgPath
		})

		saveProducts(products)
		console.log(chalk.green.inverse("New product added!"))
	}else {
		console.log(chalk.bold.red.inverse("ERROR!!!"))
		console.log(chalk.red.bold("Product name already exists!!!"))
		console.log(chalk.yellow("Please try again or update quantity."))
	}
}

const updateProduct = (quantity, name, imgPath) => {
	const products = loadProducts()

	const product = products.find((product) => product.name === name)

	if (product) {
		product.quantity = quantity
	}else {
		console.log(chalk.red.bold("No product found with that name."))
	}

	if (imgPath) {
		product.imgPath = imgPath
	}

	saveProducts(products)
}

const removeProduct = (name) => {
	const products = loadProducts()
	const productsToKeep = products.find((product) => product.name !== name)

	if (products.length > productsToKeep.length) { //Main cases
		saveProducts(productsToKeep)
		console.log(chalk.green.bold.inverse("Product removed!"))
	}else {
		console.log(chalk.bold.red.inverse("ERROR!!!"))
		console.log(chalk.red.bold("Product name not found!!!"))
	}
}

const loadProducts = () => {
	try {
		const dataBuffer = fs.readFileSync('products.json')
		const dataJSON = dataBuffer.toString()
		return JSON.parse(dataJSON)
	}catch(e) {
		return []
	}
}

const saveProducts = (product) => {
	const dataJSON = JSON.stringify(product)
	fs.writeFileSync('products.json', dataJSON)
}


module.exports = {
	addProduct: addProduct,
	updateProduct: updateProduct,
	removeProduct: removeProduct
}