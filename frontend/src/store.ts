import { browser } from "$app/env";
import { writable } from "svelte/store";


export const session = writable(
    browser && (localStorage.getItem("session") || null)
)

session.subscribe((val) => browser && (localStorage.session = val))