export default {
  template: `
    <a-date-picker
      ref="qRef"
      v-bind="$attrs"
      v-model:value="inputValue"
      :format='format'
      :valueFormat='valueFormat'
    >
      <template v-for="(_, slot) in $slots" v-slot:[slot]="slotProps">
        <slot :name="slot" v-bind="slotProps || {}" />
      </template>
    </a-date-picker>
  `,
  props: {
    value: String,
    format: String,
    valueFormat: String
  },
  data() {
    
    return {
      inputValue: dayjs(this.value, this.valueFormat) ,
    };
  },
  watch: {
    inputValue(newValue) {
      if(newValue == undefined)return;
      console.log('inputValue')
      console.log(newValue)
      this.$emit("update:value", {'date': newValue });
    },
  },
  methods: {
    updateValue() {
      this.inputValue = this.value;
    }
  }
};
