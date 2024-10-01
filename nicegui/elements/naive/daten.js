export default {
  template: `
    <n-date-picker
      ref="qRef"
      v-bind="$attrs"
      v-model:value="inputValue"
      :value-format='valueFormat'
      :format='format'
    >
      <template v-for="(_, slot) in $slots" v-slot:[slot]="slotProps">
        <slot :name="slot" v-bind="slotProps || {}" />
      </template>
    </n-date-picker>
  `,
  props: {
    value: String,
    valueFormat: String,
    format: String
  },
  data() {
    
    return {
      inputValue: dateFns.parse(this.value, this.valueFormat, new Date()),
    };
  },
  watch: {
    inputValue(newValue) {
      if(newValue == undefined)return;
      console.log('inputValue')
      console.log(newValue)
      this.$emit("update:value",{'date': dateFns.format(newValue, this.valueFormat)});
    },
  },
  methods: {
    updateValue() {
      this.inputValue = this.value;
    },
  },
};
