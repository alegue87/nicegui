export default {
  template: `
    <n-date-picker
      ref="qRef"
      v-bind="$attrs"
      v-model:value="inputValue"
    >
      <template v-for="(_, slot) in $slots" v-slot:[slot]="slotProps">
        <slot :name="slot" v-bind="slotProps || {}" />
      </template>
    </n-date-picker>
  `,
  props: {
    value: String,
    dateFormat: String,
  },
  data() {
    
    return {
      inputValue: this.value,
    };
  },
  watch: {
    inputValue(newValue) {
      if(newValue == undefined)return;
      console.log('inputValue')
      console.log(newValue)
      //this.$emit("update:value",{'date':  newValue});
    },
  },
  methods: {
    updateValue() {
      this.inputValue = this.value;
    },
  },
};
