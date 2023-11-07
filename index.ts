import { Client } from "discord.js";
import ready from "./listeners/ready";

console.log("Bot is starting...");

const client = new Client({
    intents: []
});

ready(client)

client.login(process.env.TOKEN)