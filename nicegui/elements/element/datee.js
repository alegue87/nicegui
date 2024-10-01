export default {
  template: `
    <el-date-picker
      ref="qRef"
      v-bind="$attrs"
      v-model="inputValue"
      :format='format'
      :value-format='valueFormat'
    >
      <template v-for="(_, slot) in $slots" v-slot:[slot]="slotProps">
        <slot :name="slot" v-bind="slotProps || {}" />
      </template>
    </el-date-picker>
  `,
  props: {
    value: String,
    format: String,
    valueFormat: String
  },
  data() {
    
    return {
      inputValue: this.value ,
    };
  },
  watch: {
    inputValue(newValue) {
      if(newValue == undefined)return;
      console.log('inputValue')
      console.log(newValue)
      this.$emit("update:value", {'date': newValue});
    },
  },
  methods: {
    updateValue() {
      this.inputValue = this.value;
    }
  }
};
