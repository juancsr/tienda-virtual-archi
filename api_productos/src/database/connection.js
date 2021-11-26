import sql from "mssql";
import config from "../config";

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
    const pool = await sql.connect(dbSettings);
    return pool;
  } catch (error) {
    console.error(error);
  }
};

export { sql };
