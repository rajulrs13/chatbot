<template>
  <v-app>
    <v-toolbar app color="primary">
      <v-toolbar-title v-text="title" class="white--text"></v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn class="white--text" @click="trainModel" flat>
        <v-icon left>settings</v-icon>Train
      </v-btn>
    </v-toolbar>
    <v-content>
      <router-view v-if="train"/>
      <v-layout align-center justify-center column fill-height v-else>
        <br>
        <div class="text-xs-center">
          <v-icon size="220">forum</v-icon>
        </div>
        <br>
        <h2 style="text-align:center;" class="font-weight-light">Chat Bot Needs Training</h2>
        <br>
        <h4
          style="text-align:center;"
          class="font-weight-light"
        >You can train the model by clicking on
          <v-icon size="15">settings</v-icon>
          <b>Train</b> button in the Navbar.
        </h4>
      </v-layout>
    </v-content>
    <v-snackbar v-model="snackbar" :color="snackcolor" bottom :timeout="timeout">
      {{ snacktext }}
      <v-btn dark flat @click="snackbar = false">
        <v-icon>close</v-icon>
      </v-btn>
    </v-snackbar>
    <v-dialog v-model="dialog" hide-overlay persistent width="300">
      <v-card color="primary" dark>
        <v-card-text>
          <div class="text-xs-center">{{waittext}}</div>
          <v-progress-linear indeterminate color="white" class="mb-0"></v-progress-linear>
        </v-card-text>
      </v-card>
    </v-dialog>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      train: false,
      snacktext: "Chat Bot Trained Successfully",
      title: "My Chat Bot",
      snackbar: false,
      dialog: false,
      timeout: 3000,
      snackcolor: "green",
      waittext: "Training Chat Bot... Please Wait",
      myindex:0,
      waittextlist: [
        "Training Chat Bot... Please Wait",
        "It Can Take Upto 2-5 Mins...",
        "Please Have Patience..."
      ]
    };
  },
  methods: {
    trainModel() {
      this.dialog = true;
      var payload = {
        purpose: "train"
      };
      var connectionlink = "http://192.168.1.7:8000/getreply";
      var config = {
        headers: {
          "Content-Type": "multipart/form-data",
          "Access-Control-Allow-Origin": "*"
        }
      };
      self = this;
      axios
        .post(connectionlink, payload, config)
        .then(function(response) {
          self.dialog = false;
          if (response.data.code == "success") {
            self.train = true;
            self.snacktext = "Chat Bot Trained Successfully";
            self.snackcolor = "green";
            self.snackbar = true;
          } else {
            self.train = false;
            self.snacktext = "Something Went Wrong. Please Try Again.";
            self.snackcolor = "red";
            self.snackbar = true;
          }
        })
        .catch(function() {
          self.dialog = false;
          self.train = false;
          self.snacktext = "Something Went Wrong. Please Try Again.";
          self.snackcolor = "red";
          self.snackbar = true;
        });
      setInterval(() => {
        this.waittext = this.waittextlist[this.myindex];
        this.myindex = this.myindex + 1;
        if(this.myindex >= this.waittextlist.length){
          this.myindex = 0;
        }
      }, 3500);
    }
  },
  name: "App"
};
</script>
