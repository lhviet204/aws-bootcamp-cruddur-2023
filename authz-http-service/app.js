const express = require("express");
const app = express();
const port = 9002;

const { CognitoJwtVerifier } = require("aws-jwt-verify");

// Verifier that expects valid access tokens:
const jwtVerifier = CognitoJwtVerifier.create({
    userPoolId: process.env.AWS_COGNITO_USER_POOL_ID,
    tokenUse: process.env.AWS_COGNITO_USER_POOL_CLIENT_ID,
    clientId: "",
});

app.get("*", async (req, res, next) => {
    try{
      const payload = await jwtVerifier.verify(req.header("authorization"));
    } catch (err) {
      console.error(err);
      return res.status(403).json({ statusCode: 403, message: "Forbidden" });
    }
    console.log("JWT Token is valid. Token:  ", payload)
    res.append('x-cognito-username', payload.username);   
});

// Hydrate the JWT verifier, then start express.
// Hydrating the verifier makes sure the JWKS is loaded into the JWT verifier,
// so it can verify JWTs immediately without any latency.
// (Alternatively, just start express, the JWKS will be downloaded when the first JWT is being verified then)
jwtVerifier
  .hydrate()
  .catch((err) => {
    console.error(`Failed to hydrate JWT verifier: ${err}`);
    process.exit(1);
  })
  .then(() =>
    app.listen(port, () => {
      console.log(`Example app listening at http://localhost:${port}`);
    })
  );