<template>
  <v-card hover @click="toSyllabus" outlined>
    <v-container>
      <v-row>
        <v-col class="title_text">{{syllabus.subject_name}}</v-col>
      </v-row>
      <v-row>
        <v-col class="little_text">
          {{teachers}}
        </v-col>
      </v-row>
      <v-row class="icon-row pt-2" no-gutters>
        <v-col xl="2" lg="4n">
          <v-img width="24" height="24" :src="fieldImg" />
        </v-col>
        <v-col xl="2" lg="4n">
          <v-img width="24" height="24" :src="methodImg" />
        </v-col>
        <v-col xl="2" lg="4n" v-if="syllabus.term !== '通期'">
          <v-img width="24" height="24" :src="termImg" />
        </v-col>
        <v-col xl="2" lg="4n" v-if="syllabus.is_giga">
          <v-img width="24" height="24" :src="gigaImg" />
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script lang="ts">
import {Component, Prop, Vue} from "nuxt-property-decorator";
import {Subject} from "@/pages/Types"
import {fieldIcon, giga_icon, methodIcon, termIcon} from "~/pages/Tools";

@Component
export default class SyllabusCard extends Vue{
  @Prop({type: Object, required: true})
  syllabus!: Subject;

  toSyllabus(){
    window.open(this.syllabus.url);
  }

  get fieldImg(){
    return fieldIcon(this.syllabus.field);
  }

  get methodImg(){
    return methodIcon(this.syllabus.method);
  }

  get termImg(){
    return termIcon(this.syllabus.term);
  }

  get gigaImg(){
    return giga_icon;
  }

  get teachers(){
    let s = ""
    const teachers = this.syllabus.staff;
    for(let i = 0; i < 3 && i < teachers.length; i++){

      s += teachers[i] + ((i === 2 || i === teachers.length - 1) ? "" : ", ");
    }
    if(teachers.length >= 3)
      s += "等"
    return s;
  }
}
</script>

<style scoped>

.title_text {
  font-size: 0.8em;
}

.little_text{
  font-size: 0.5em;
}

.icon-row {
  align-items: center;
}

</style>
