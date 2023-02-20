<template>
    <div class="csv-table-row">
        <div class="row__cell">
            {{ row_data._source.customers_id }}
        </div>
        <div class="row__cell">
            {{ row_data._source.customers_firstname }}
        </div>
        <div class="row__cell">
            {{ row_data._source.customers_lastname }}
        </div>
        <div class="row__cell">
            {{ row_data._source.customers_email_address }}
        </div>
    </div>
</template>

<script>
export default {
    name: "csv-table-row",
    props: {
        row_data: {
            type: Object,
            default() {
                return {};
            },
        },
    },
};
</script>

<style lang="scss">
@import "~@/assets/variables.scss";
.csv-table-row {
    display: flex;
    justify-content: space-between;
    padding: $padding;
    margin-bottom: $padding;
    border: solid 1px #e4e4e4;
    border-radius: $border-radius;
    background: $light-white-bg;
    &:hover {
        background: $light-yellow-bg;
    }
    .row {
        &__cell {
            flex: 1 1 20%;
            text-align: center;
        }
    }
}
</style>
