<template>
    <div id="app">
        <csv-info />
    </div>
</template>

<script>
import csvInfo from "./components/csv-table/csv-info";
export default {
    name: "app",
    components: {
        csvInfo,
    },
};
</script>

<style lang="scss">
@import "~@/assets/variables.scss";
div {
    font-size: $main-font-size;
}
</style>
