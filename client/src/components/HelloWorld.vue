<template>
  <v-container>
    <v-layout row wrap class="mb-5">
      <v-flex xs12 sm8 offset-sm2>
        <div id="msgbox">
          <div v-for="(message,index) in messageList" :key="index">
            <!-- Bot Msg -->
            <div class="my-3" v-if="message.sender == 'bot'">
              <v-layout row spacer align-center wrap>
                <v-flex xs2 class="text-xs-center">
                  <v-avatar color="primary">
                    <v-icon dark>bubble_chart</v-icon>
                  </v-avatar>
                </v-flex>

                <v-flex xs10>
                  <p class="text-xs-left ml-1 px-2 py-2">{{ message.msg }}</p>
                </v-flex>
              </v-layout>
            </div>

            <!-- User Msg -->
            <div class="my-3" v-else>
              <v-layout row spacer align-center>
                <v-flex xs10>
                  <p class="text-xs-right mr-1 px-2 py-2">{{ message.msg }}</p>
                </v-flex>
                <v-flex xs2 class="text-xs-center">
                  <v-avatar color="green">
                    <v-icon dark>perm_identity</v-icon>
                  </v-avatar>
                </v-flex>
              </v-layout>
            </div>
          </div>
        </div>
      </v-flex>
    </v-layout>
    <v-footer fixed height="80" color="#ECEFF1">
      <v-layout row wrap class="mt-3">
        <v-flex xs10 sm6 offset-sm3 offset-xs1>
          <v-text-field
            :disabled="isdisabled"
            v-model="message"
            append-outer-icon="send"
            box
            clear-icon="close-circle"
            clearable
            label="Enter Your Message"
            type="text"
            @click:append-outer="sendMessage"
            @keyup.enter="sendMessage"
            @click:clear="clearMessage"
          ></v-text-field>
        </v-flex>
      </v-layout>
    </v-footer>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    message: "",
    messageList: [
      {
        sender: "bot",
        msg: "Hello! My name is Sintel. You can ask my anything."
      }
    ],
    isdisabled: false
  }),
  methods: {
    sendMessage() {
      if (this.message.trim().length > 0) {
        this.loading = true;
        this.isdisabled = true;
        var payload = {
          purpose: "query",
          message: this.message.trim()
        };
        var connectionlink = "http://192.168.1.7:8000/getreply";
        var config = {
          headers: {
            "Content-Type": "multipart/form-data",
            "Access-Control-Allow-Origin": "*"
          }
        };
        self = this;
        axios.post(connectionlink, payload, config).then(function(response) {
          var reply = response.data.chatbot_message;
          self.addmsg("bot", reply);
          self.isdisabled = false;
        });
        this.addmsg("you", this.message);
        this.scrollToBottom();
      }
      this.clearMessage();
    },
    clearMessage() {
      this.message = "";
    },
    addmsg(sendby, message) {
      this.messageList.push({ sender: sendby, msg: message });
    },
    scrollToBottom() {
      var objDiv = document.getElementById("msgbox");
      objDiv.scrollTop = objDiv.scrollHeight;
    }
  }
};
</script>

