/* 
Main Components:
	Product
		Product Number + Double Check
		Product Picture (PH file path)
		Price (Updates)
		Quantity (Updates)
	Users
		Name
		Email
		Password (Encrypted by some simple algorithm)
		USER# (RNG + Double check)
	Functions
		Product
			Quantity Update
			Price Update
		Users
			Email update
			Pass Update
Bonus Components:
	GUI
	Implement to a database
*/

const fs = require('fs')
const chalk = require('chalk')
const yargs = require('yargs')

const products = require('./product.js')
const users = require('./users.js')

//Product Add
yargs.command({
	command: 'addProduct',
	describe: 'Adding Product',
	builder: {
		num: {
			describe: 'Product Number',
			demandOption: false,
			type: 'string'
		},
		name: {
			describe: 'Product Name',
			demandOption: true,
			type: 'string'
		},
		imgPath: {
			describe: 'Image Path for the Product',
			demandOption: false,
			type: 'string'
		}
	},
	handler (argv) {
		products.addProduct(argv.num, argv.name, argv.imgPath)
	}
})

//Product Update
yargs.command({
	command: 'updateProduct',
	describe: 'Updating Product',
	builder: {
		quantity: {
			describe: 'Quantity Update',
			demandOption: true,
			type: 'string'
		},
		name: {
			describe: 'Product Name',
			demandOption: true,
			type: 'string'
		},
		imgPath: {
			describe: 'Image Path for the Product',
			demandOption: false,
			type: 'string'
		}
	},
	handler (argv) {
		products.updateProduct(argv.quantity, argv.name, argv.imgPath)
	}
})

//Product Delete
yargs.command({
	command: 'removeProduct',
	describe: 'Removing Product',
	builder: {
		name: {
			describe: 'Product Name',
			demandOption: true,
			type: 'string'
		}
	},
	handler (argv) {
		products.removeProduct(argv.name)
	}
})


//USERS

//User Add
yargs.command({
	command: 'addUser',
	describe: 'Adding User',
	builder: {
		name: {
			describe: 'User Name',
			demandOption: true,
			type: 'string'
		},
		email: {
			describe: 'User E-mail',
			demandOption: true,
			type: 'string'
		},
		password: {
			describe: 'User Password',
			demandOption: true,
			type: 'string'
		}
	},
	handler (argv) {
		users.addUser(argv.name, argv.email, argv.password)
	}
})

//User Update
//User Remove
//User Ban (includes remove)
yargs.command({
	command: 'banUser',
	describe: 'Banning User',
	builder: {
		name: {
			describe: 'User Name',
			demandOption: true,
			type: 'string'
		},
		email: {
			describe: 'User E-mail',
			demandOption: false,
			type: 'string'
		}
	},
	handler (argv) {
		users.banUser(argv.name, argv.email)
	}
})


yargs.parse()