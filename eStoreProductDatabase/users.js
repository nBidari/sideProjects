const fs = require('fs')
const chalk = require('chalk')

const addUser = (name, email, pass) => {
    const users = loadUsers()

    
}

const encryptPass = (pass) => {

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
    addUser: addUser
}