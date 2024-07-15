// stores/socketStore.js
import { defineStore } from 'pinia'
import { io } from 'socket.io-client'

export const useSocketStore = defineStore('socket', {
  state: () => ({
    messages: [],
    socket: null
  }),
  actions: {
    initializeSocket() {
      console.log('try connectiong')
      this.socket = io('http://127.0.0.1:8000')
      this.socket.on('chat', (message) => {
        console.log(message)
        this.messages.push(message)
      })
    },
    sendMessage(message) {
      this.socket.emit('chat', message)
    }
  }
})
