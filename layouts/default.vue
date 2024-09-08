<template>
  <v-app dark>
    <v-app-bar
      fixed
      app
      hide-on-scroll
    >
      <v-list-item-title>SFCシラバス検索</v-list-item-title>
      <v-switch v-model="listView" label="リスト表示" class="switch-list" inset hide-details></v-switch>
    </v-app-bar>
    <v-main>
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>
    <v-app-bar>
      <v-spacer></v-spacer>
      <v-toolbar-title><a href="https://github.com/kota-yata/Syllabus-proto">GitHub</a></v-toolbar-title>
      <v-spacer></v-spacer>
    </v-app-bar>
<!--    <v-navigation-drawer-->
<!--      v-model="rightDrawer"-->
<!--      temporary-->
<!--      fixed-->
<!--      right-->
<!--    >-->
<!--      <v-list>-->

<!--      </v-list>-->
<!--    </v-navigation-drawer>-->
  </v-app>
</template>

<script lang="ts">
import { Component, Vue, Watch } from "nuxt-property-decorator";
import SearchNav from "~/components/Navigation/SearchNav.vue";

@Component({
  components: {SearchNav}
})
export default class DefaultLayout extends Vue{
  listView = false;
  @Watch('listView')
  onSwitchValueChange() {
    this.$store.commit('setListView', this.listView);
  }
}
</script>

<style scoped>
  .switch-list {
    min-width: 150px;
  }
  .switch-list >>> .v-label {
    font-size: 0.9rem;
  }
</style>
