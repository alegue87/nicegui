const menuOptions = [
  {
    label: "Hear the Wind Sing",
    key: "hear-the-wind-sing",
    href: "https://en.wikipedia.org/wiki/Hear_the_Wind_Sing"
  },
  {
    label: "Pinball 1973",
    key: "pinball-1973",
    disabled: true,
    icon: "pinwheel",
    children: [
      {
        label: "Rat",
        key: "rat",
      }
    ]
  },
  {
    label: "A Wild Sheep Chase",
    key: "a-wild-sheep-chase",
    disabled: true,
    icon: "gesture-pinch"
  },
  {
    label: "Dance Dance Dance",
    key: "Dance Dance Dance",
    children: [
      {
        type: "group",
        label: "People",
        key: "people",
        children: [
          {
            label: "Narrator",
            key: "narrator"
          },
          {
            label: "Sheep Man",
            key: "sheep-man"
          }
        ]
      },
      {
        label: "Beverage",
        key: "beverage",
        children: [
          {
            label: "Whisky",
            key: "whisky",
            href: "https://en.wikipedia.org/wiki/Whisky"
          }
        ]
      },
      {
        label: "Food",
        key: "food",
        children: [
          {
            label: "Sandwich",
            key: "sandwich"
          }
        ]
      },
      {
        label: "The past increases. The future recedes.",
        key: "the-past-increases-the-future-recedes"
      }
    ]
  }
];

import AnchorNve from './anchorn.js'

export default {
  template: `
    <n-menu
      :options='options'
      :render-label="renderMenuLabel"
      :render-icon="renderMenuIcon"
      :expand-icon="expandIcon"
    >
      <template v-for="(_, slot) in $slots" v-slot:[slot]="slotProps">
        <slot :name="slot" v-bind="slotProps || {}" />
      </template>
    </n-menu>
  `,
  props: {
    optionsValue: Array
  },
  data() { 
    return {
      options: this.optionsValue,
    };
  },
  methods: {
    emit(key, path, href){
      this.$emit("click:value",{key: key, path: path})
    },
    renderMenuLabel(option) {
      return Vue.h(AnchorNve, { label: option.label, keyV: option.key, href: option.href, path: option.path, emit: this.emit });
    },
  },
  setup() {
    app.$refs.menu = this

    return {
      menuOptions,
      collapsed: false,
     
      renderMenuIcon(option) {
        //console.log(option)
        if(option.icon === undefined ) {
          return Vue.h('span', {class:'mdi mdi-circle-medium'}, { default: () => Vue.h('span') });
        }
        else {
          return Vue.h('span', {class:'mdi mdi-'+option.icon}, { default: () => Vue.h('span') });

        }
      },
      expandIcon() {
        return  Vue.h('span', {class:'mdi mdi-chevron-down'}, { default: () => Vue.h('span') });
      }
    };
  }
};
