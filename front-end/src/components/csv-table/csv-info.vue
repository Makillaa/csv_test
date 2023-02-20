<template>
    <div class="csv-info">
        <csv-info-table />
    </div>
</template>
<script>
import csvInfoTable from "./csv-info-table";

export default {
    name: "csv-info",
    components: {
        csvInfoTable,
    },
};
</script>

<style lang="scss">
@import "~@/assets/variables.scss";
.csv-info {
    margin: $padding * 3 auto;
    padding: $padding $padding * 2;
    border-radius: $border-radius * 2;
    max-width: 990px;
}
</style>
