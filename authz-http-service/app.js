import { CognitoJwtVerifier } from "aws-jwt-verify";

// Verifier that expects valid access tokens:
const verifier = CognitoJwtVerifier.create({
    userPoolId: process.env.AWS_COGNITO_USER_POOL_ID,
    tokenUse: process.env.AWS_COGNITO_USER_POOL_CLIENT_ID,
    clientId: "",
});

const http = require('node:http');

// Create an HTTP server
const server = http.createServer((req, res) => {
   try{
        const authHeader = req.getHeader('Authorization')
        let payload

        if (authHeader && authHeader.split(' ')[0] === 'Bearer'){
            payload = verifier.verify(authHeader.split(' ')[1]);
        } else {
            payload = verifier.verify(authHeader);
        }
        console.log("JWT Token is valid. Token:  ", payload)
        res.setHeader('x-cognito-username', payload.username);
    } catch (err) {
    console.error(err);
    return res.status(200).end()
    }    
});

server.listen(9002)
