<script setup>
import { ref, onMounted, computed } from 'vue';
import { useSocketStore } from './stores/socketStore';

const socketStore = useSocketStore();
const newMessage = ref('');

onMounted(() => {
  socketStore.initializeSocket();
});

const sendMessage = () => {
  socketStore.sendMessage(newMessage.value);
  newMessage.value = '';
};

const messages = computed(() => socketStore.messages);
</script>

<template>
  <div>
    <h1>Messages</h1>
    <ul>
      <li v-for="message in messages" :key="message.sid">{{ message.message }}</li>
    </ul>
    <input v-model="newMessage" @keyup.enter="sendMessage" placeholder="Type a message" />
  </div>
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
