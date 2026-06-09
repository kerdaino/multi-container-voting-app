require("dotenv").config();
const { Pool } = require("pg");

const pool = new Pool({
  host: process.env.DB_HOST || "db",
  database: process.env.DB_NAME || "voting_db",
  user: process.env.DB_USER || "postgres",
  password: process.env.DB_PASSWORD || "postgres",
  port: process.env.DB_PORT || 5432,
});

async function processVotes() {
  try {
    const result = await pool.query(`
      SELECT option_name, COUNT(*) AS total_votes
      FROM votes
      GROUP BY option_name
    `);

    console.log("Current vote results:");

    if (result.rows.length === 0) {
      console.log("No votes yet.");
    } else {
      result.rows.forEach((row) => {
        console.log(`${row.option_name}: ${row.total_votes} votes`);
      });
    }

    console.log("--------------------------");
  } catch (error) {
    console.error("Worker error:", error.message);
  }
}

console.log("Worker service started...");

setInterval(processVotes, 5000);