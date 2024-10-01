export default {
  template: `
    <p-date
      ref="qRef"
      v-bind="$attrs"
      v-model="inputValue"
    >
      <template v-for="(_, slot) in $slots" v-slot:[slot]="slotProps">
        <slot :name="slot" v-bind="slotProps || {}" />
      </template>
    </p-date>
  `,
  props: {
    value: String,
    dateFormat: String,
  },
  data() {
    
    return {
      inputValue: dateFns.parse(this.value, this.dateFormat, new Date()) ,
    };
  },
  watch: {
    inputValue(newValue) {
      if(newValue == undefined)return;
      console.log('inputValue')
      console.log(newValue)
      this.$emit("update:value",{'date':  dateFns.format(newValue, this.dateFormat)});
    },
  },
  methods: {
    updateValue() {
      this.inputValue = this.value;
    }
  }
};
