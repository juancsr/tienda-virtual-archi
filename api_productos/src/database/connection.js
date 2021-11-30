/*import sql from "mssql";*/
//import config from "../config";
const sqlite3 = require('sqlite3').verbose();
const pool = new sqlite3.Database('./database/db.sqlite')

export const dbSettings = {
  user: "testSa",
  password: "S3cur1t4s+2020.",
  server: "srvdesarrollo",
  database: "webstore",
  options: {
    encrypt: true, // for azure
    trustServerCertificate: true, // change to true for local dev / self-signed certs
  },
};

export const getConnection = async () => {
  try {
    const pool = new sqlite3.Database('./database/db.sqlite')
    
    return pool;
  } catch (error) {
    console.error(error);
  }
};

export { pool };
