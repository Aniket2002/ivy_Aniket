from hypothesis import given
# local
import ivy_tests.test_ivy.helpers as helpers
from ivy_tests.test_ivy.helpers import handle_cmd_line_args


# split
@handle_cmd_line_args
@given(
    dtype_x_axis=helpers.dtype_values_axis(
        available_dtypes=helpers.get_dtypes("numeric"),
        min_axis=-1,
        max_axis=0,
        min_num_dims=1,
        force_int_axis=True,
    ),
    num_positional_args=helpers.num_positional_args(
        fn_name="ivy.functional.frontends.numpy.split"
    ),
)
def test_numpy_split(
    dtype_x_axis,
    as_variable,
    num_positional_args,
    native_array,
):
    indices_or_sections, ary, axis = dtype_x_axis
    helpers.test_frontend_function(
        as_variable_flags=as_variable,
        with_out=False,
        num_positional_args=num_positional_args,
        native_array_flags=native_array,
        frontend="numpy",
        fn_tree="split",
        ary=ary[0],
        axis=axis,
        indices_or_sections = indices_or_sections[0],
    )
