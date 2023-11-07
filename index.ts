import { Client } from "discord.js";

console.log("Bot is starting...");

const client = new Client({
    intents: []
});

client.login(process.env.TOKEN)

console.log(client); 