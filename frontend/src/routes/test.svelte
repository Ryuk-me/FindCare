<script>
    import { useForm, Hint, validators, minLength } from "svelte-use-form";
  
    const form = useForm();
  </script>
  
  <form use:form>
    <input name="title" use:validators={[minLength(5)]} />
    <Hint for="title" on="minLength" let:value>
      The title requires at least {value} characters.
    </Hint>
  
    <button disabled={!$form.valid}>Submit</button> <br />
  </form>