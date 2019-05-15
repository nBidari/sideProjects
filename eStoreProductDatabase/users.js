const fs = require('fs')
const chalk = require('chalk')
const crypto = require('crypto')

const addUser = (name, email, pass) => {
    const users = loadUsers()

	const nameDuplicates = users.find((user) => user.name === name)
	const emailDuplicates = users.find((userEmail) => userEmail.email === email)
	const emailValidate = validateEmail(email)

	if (!nameDuplicates && !emailDuplicates) {
		const newPass = encryptPass(pass)
		users.push({
			name: name,
			email: email,
			pass: newPass
		})

		saveUsers(users)
		console.log(chalk.green.inverse("New user added!"))
	}else {
		console.log(chalk.bold.red.inverse("ERROR!!!"))
		console.log(chalk.red.bold("User already exists!!!"))
		console.log(chalk.yellow("Please try again with different name."))
	}
}

const banUser = (name, email) => {
	const blacklist = loadBlackList()

	const nameDuplicates = blacklist.find((user) => user.name === name)
	const emailDuplicates = blacklist.find((userEmail) => userEmail.email === email)

	if (!nameDuplicates && !emailDuplicates) {
		blacklist.push({
			name: name,
			email: email
		})

		
		saveUserBlacklist(blacklist)
		console.log(chalk.yellow.bold("BAN HAMMER!!!!"))
	}else {
		console.log(chalk.bold.red.inverse("ERROR!!!"))
		console.log(chalk.red.bold("User already banned!!!"))
		console.log(chalk.yellow("Please check the name again!"))
	}
}

const encryptPass = (pass) => {
	let algorithm = 'aes-256-cbc'
	let key = crypto.randomBytes(32)
	let iv = crypto.randomBytes(16)

	let cipher = crypto.createCipheriv(algorithm, Buffer.from(key), iv)
	let encrypted = cipher.update(pass)
	encrypted = Buffer.concat([encrypted, cipher.final()])
	return { iv: iv.toString('hex'), encryptedData: encrypted.toString('hex'), key: key};
}

const decryptPass = (pass) => {
	let iv = Buffer.from(pass.iv, 'hex')
	let encryptedText = Buffer.from(pass.encryptedData, 'hex')
	let decipher = crypto.createDecipheriv('aes-256-cbc', Buffer.from(pass.key), iv)
	let decrypted = decipher.update(encryptedText)
	decrypted = Buffer.concat([decrypted, decipher.final()])
	return decrypted.toString()
}

const validateEmail = (email) => {

}

const checkBlackList = (email) => {

}

const loadUsers = () => {
    try {
		const dataBuffer = fs.readFileSync('users.json')
		const dataJSON = dataBuffer.toString()
		return JSON.parse(dataJSON)
	}catch(e) {
		return []
	}
}

const loadBlackList = () => {
    try {
		const dataBuffer = fs.readFileSync('user-blacklist.json')
		const dataJSON = dataBuffer.toString()
		return JSON.parse(dataJSON)
	}catch(e) {
		return []
	}
}

const saveUsers = (users) => {
    const dataJSON = JSON.stringify(users)
	fs.writeFileSync('users.json', dataJSON)
}

const saveUserBlacklist = (users) => {
    const dataJSON = JSON.stringify(users)
	fs.writeFileSync('user-blacklist.json', dataJSON)
}
module.exports = {
	addUser: addUser,
	banUser: banUser
}