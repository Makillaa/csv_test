<template>
    <div class="header__item">ID</div>
</template>
<script>
import { mapGetters, mapActions } from "vuex";
import axios from "axios";
import csvTableRow from "./csv-table-row";
export default {
    name: "csv-info-table",
    components: {
        csvTableRow,
    },
    data: () => {
        return {
            searchFiledValue: null,
        };
    },
    computed: {
        ...mapGetters(["csvS", "CSV_INFO"]),
    },
    methods: {
        ...mapActions([
            "GET_ES_INFO",
            "GET_csvS_FROM_API",
            "GET_csvS_BY_SEARCH_RESULTS",
        ]),
        getESInfo(search) {
            this.GET_ES_INFO(search);
        },
        onSearch() {
            this.getESInfo(this.searchFiledValue);
        },
    },
    mounted() {
        this.getESInfo();
    },
};
</script>

<style lang="scss">
@import "~@/assets/variables.scss";
.csv-info-table {
    margin: $padding * 3 auto;
    padding: $padding;
    background: $light-grey-bg;
    border-radius: $border-radius * 2;
    box-shadow: 0 0 20px 0px #949494;
    & .table__header {
        display: flex;
        justify-content: space-between;
        padding: $padding;
    }

    .search {
        &__field {
            margin-right: $padding;
            & input {
                border: solid 1px #e4e4e4;
                padding: $padding/2;
                border-radius: $border-radius;
                outline: none;
            }
        }

        &__button {
            background-color: rgba(51, 51, 51, 0.05);
            border-radius: 8px;
            border-width: 0;
            color: #333333;
            cursor: pointer;
            display: inline-block;
            margin-left: 20px;
            padding: 10px 12px;
            text-align: center;
            vertical-align: baseline;
            white-space: nowrap;
            user-select: none;
        }
    }

    .header {
        &__item {
            flex: 1 1 20%;
            text-align: center;
        }
    }
}
</style>
