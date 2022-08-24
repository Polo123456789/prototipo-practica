<template>
  <div>
    Mensaje desde el servidor: {{msg}}
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import {Context} from '@nuxt/types';

export default Vue.extend({
  name: 'IndexPage',
  async asyncData({$axios}: Context) {
    const msg = await $axios.$get('/api/hello');
    return { msg };
  }
})
</script>
