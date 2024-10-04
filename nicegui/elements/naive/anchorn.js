export default {
    template: `
      <a
        @click='onClick'
        :href='this.href'
      >
        {{this.label}}
      </a>
    `,
    props: {
        keyV: String,
        label: String,
        href: String,
        path: String,
        emit: Function
    },
    data() { 
      return {

      };
    },
    methods: {
        onClick(){
            this.emit(this.key, this.path)
        }
    },
    setup() {
  
    }
  };
