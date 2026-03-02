---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:4320
- loss:CosineSimilarityLoss
base_model: sentence-transformers/all-MiniLM-L6-v2
widget:
- source_sentence: Include vitamin C-rich foods. Incorporate foods high in vitamin
    C, such as citrus fruits, leafy greens, and bell peppers, into your diet.
  sentences:
  - Romantic Partnerships and Intimacy. Romantic partnerships involve a dynamic interplay
    between intimacy and power. Here are ways to maintain a healthy balance in your
    partnership.
  - Using Technology to Enhance Accessibility in Education. Technology has the potential
    to significantly enhance accessibility in education, but it can also create new
    barriers if not designed with accessibility in mind. This article explores the
    key considerations for designing accessible educational technology and provides
    strategies for educators to incorporate accessibility into their teaching practices.
  - Nutrition for Optimal Immune Function. The food we eat plays a significant role
    in maintaining a healthy immune system. A balanced diet rich in essential nutrients
    can help boost the immune system, reduce inflammation, and increase the production
    of white blood cells. Include foods high in vitamins C and D, antioxidants, and
    omega-3 fatty acids to support immune function.
- source_sentence: Review and Adjust. Regularly reassess your goals, adjust your strategy,
    and make adjustments as needed
  sentences:
  - The Importance of Setting Realistic Expectations. Setting realistic expectations
    is essential for maintaining mental and emotional health. Prioritize activities
    that promote realistic expectations, such as practicing self-compassion, challenging
    negative thoughts, and developing coping skills.
  - Maximizing Your Learning with Accountability. Accountability is a key component
    of academic success. By setting clear goals, tracking progress, and maintaining
    regular check-ins with a support network, you can stay focused, motivated, and
    directed towards your objectives. Regularly practicing accountability will also
    help you stay on track, overcome obstacles, and achieve your goals.
  - The Importance of Understanding Your Insurance Needs. Having the right insurance
    coverage is essential for protecting your assets, income, and loved ones. This
    article provides an overview of the importance of understanding your insurance
    needs. Consider factors like income replacement, liability, and legacy planning.
- source_sentence: Inspect and review the home thoroughly. Hire inspectors, appraisers,
    and review contracts carefully to avoid costly surprises or hidden issues
  sentences:
  - 'Communication is Key in Healthy Relationships. Effective communication is a vital
    aspect of any relationship. By expressing your thoughts and feelings openly and
    honestly, you can avoid misunderstandings and build trust with your partner. Here
    are three key strategies to improve communication in your relationship: ...'
  - Navigating the Homebuying Process. Buying a home can be a daunting experience,
    but with the right guidance, you'll be well-equipped to navigate the process.
    Our article covers essential steps, from budgeting and credit checks to mortgage
    applications and closing. With these insider tips, you'll be ready to make a confident
    offer and secure the keys to your dream home.
  - The Importance of Boundaries in Relationships. Setting healthy boundaries is crucial
    in any relationship. Boundaries help maintain respect, trust, and a sense of independence.
    Healthy boundaries also help prevent resentment and feelings of suffocation. Here
    are some examples of how boundaries can be beneficial in a relationship.
- source_sentence: Develop a pre-test routine. Establish a consistent routine that
    calms their nerves and prepares them for the test.
  sentences:
  - 'The Benefits of Morning Exercise. Starting your day with exercise can have a
    significant impact on your mental and emotional well-being. By incorporating morning
    exercise into your routine, you can reduce stress, improve your mood, and even
    increase feelings of joy and happiness. Here are some benefits of morning exercise:
    Improves circulation and reduces stress. Boosts energy and alertness. Enhances
    focus and concentration. Supports weight loss by increasing caloric burn. Improves
    overall physical health and well-being.'
  - 'The Benefits of Nature Therapy. Spending time in nature can have a significant
    impact on your mental and emotional well-being. By incorporating nature therapy
    into your life, you can reduce stress, improve your mood, and even lower your
    blood pressure. Here are some of the benefits of nature therapy: Reduces stress
    and anxiety. Improves sleep quality. Enhances focus and concentration. Boosts
    mood and reduces symptoms of depression. Improves relationships by increasing
    empathy and compassion. Supports weight loss by reducing stress-eating.'
  - Overcoming Test Anxiety and Building Confidence. Test anxiety is a common challenge
    that many students face. However, with the right strategies, students can overcome
    anxiety and build confidence. This includes developing a pre-test routine, practicing
    relaxation techniques, and reframing negative thoughts.
- source_sentence: Research the business. Thoroughly research the small business,
    including its financials, management team, and market potential.
  sentences:
  - How to Write a Resume. Writing a resume can be a challenging task, but it's essential
    to showcase your skills and experiences to potential employers. In this article,
    we will guide you on how to write a resume. First, define your target audience
    and tailor your resume accordingly. Second, create a professional summary that
    highlights your skills and experiences. Third, use a clear and concise format
    to present your information. Fourth, include relevant work experience, education,
    and skills. Fifth, proofread and edit your resume to ensure it's error-free and
    effective.
  - 10 Signs of a Toxic Relationship. A toxic relationship can have devastating consequences
    on your physical and emotional health. If you're unsure whether your relationship
    is healthy or not, look out for these warning signs.
  - The Benefits of Investing in a Small Business. Investing in a small business can
    provide tax benefits, diversification, and potential returns on investment. Here
    are three benefits of investing in a small business.
pipeline_tag: sentence-similarity
library_name: sentence-transformers
---

# SentenceTransformer based on sentence-transformers/all-MiniLM-L6-v2

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2). It maps sentences & paragraphs to a 384-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) <!-- at revision c9745ed1d9f207416be6d2e6f8de32d1f16199bf -->
- **Maximum Sequence Length:** 256 tokens
- **Output Dimensionality:** 384 dimensions
- **Similarity Function:** Cosine Similarity
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 256, 'do_lower_case': False, 'architecture': 'BertModel'})
  (1): Pooling({'word_embedding_dimension': 384, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
  (2): Normalize()
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    'Research the business. Thoroughly research the small business, including its financials, management team, and market potential.',
    'The Benefits of Investing in a Small Business. Investing in a small business can provide tax benefits, diversification, and potential returns on investment. Here are three benefits of investing in a small business.',
    "How to Write a Resume. Writing a resume can be a challenging task, but it's essential to showcase your skills and experiences to potential employers. In this article, we will guide you on how to write a resume. First, define your target audience and tailor your resume accordingly. Second, create a professional summary that highlights your skills and experiences. Third, use a clear and concise format to present your information. Fourth, include relevant work experience, education, and skills. Fifth, proofread and edit your resume to ensure it's error-free and effective.",
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.9847, 0.9795],
#         [0.9847, 1.0000, 0.9681],
#         [0.9795, 0.9681, 1.0000]])
```

<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset

* Size: 4,320 training samples
* Columns: <code>sentence_0</code>, <code>sentence_1</code>, and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence_0                                                                         | sentence_1                                                                         | label                                                         |
  |:--------|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|:--------------------------------------------------------------|
  | type    | string                                                                             | string                                                                             | float                                                         |
  | details | <ul><li>min: 10 tokens</li><li>mean: 27.32 tokens</li><li>max: 57 tokens</li></ul> | <ul><li>min: 9 tokens</li><li>mean: 70.99 tokens</li><li>max: 256 tokens</li></ul> | <ul><li>min: 1.0</li><li>mean: 1.0</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                           | sentence_1                                                                                                                                                                                                                                                                                                                       | label            |
  |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
  | <code>Create a savings plan. Create a savings plan, including setting a realistic timeline, prioritizing expenses, and automating savings to reach your goal.</code> | <code>How to Create a Budget for a Down Payment on a House. Creating a budget for a down payment on a house requires saving and disciplining yourself to save a significant amount of money. Here are three steps to create a budget for a down payment on a house.</code>                                                       | <code>1.0</code> |
  | <code>Limit processed and sugary foods. Limit or avoid processed and sugary foods that can negatively impact brain health.</code>                                    | <code>Nutrition for Optimal Brain Function. The food we eat has a direct impact on our brain function. A balanced diet rich in essential nutrients can improve cognitive function, boost mood, and increase energy levels. Include foods high in omega-3 fatty acids, antioxidants, and vitamins to support brain health.</code> | <code>1.0</code> |
  | <code>Diversify your portfolio. Consider diversifying your investment portfolio by investing in a small business to reduce reliance on a single investment.</code>   | <code>The Benefits of Investing in a Small Business. Investing in a small business can provide tax benefits, diversification, and potential returns on investment. Here are three benefits of investing in a small business.</code>                                                                                              | <code>1.0</code> |
* Loss: [<code>CosineSimilarityLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cosinesimilarityloss) with these parameters:
  ```json
  {
      "loss_fct": "torch.nn.modules.loss.MSELoss"
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 16
- `num_train_epochs`: 1
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `do_predict`: False
- `eval_strategy`: no
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 16
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 5e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1
- `num_train_epochs`: 1
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: None
- `warmup_ratio`: None
- `warmup_steps`: 0
- `log_level`: passive
- `log_level_replica`: warning
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `enable_jit_checkpoint`: False
- `save_on_each_node`: False
- `save_only_model`: False
- `restore_callback_states_from_checkpoint`: False
- `use_cpu`: False
- `seed`: 42
- `data_seed`: None
- `bf16`: False
- `fp16`: False
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `local_rank`: -1
- `ddp_backend`: None
- `debug`: []
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_prefetch_factor`: None
- `disable_tqdm`: False
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch_fused
- `optim_args`: None
- `group_by_length`: False
- `length_column_name`: length
- `project`: huggingface
- `trackio_space_id`: trackio
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `skip_memory_metrics`: True
- `push_to_hub`: False
- `resume_from_checkpoint`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_private_repo`: None
- `hub_always_push`: False
- `hub_revision`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `include_for_metrics`: []
- `eval_do_concat_batches`: True
- `auto_find_batch_size`: False
- `full_determinism`: False
- `ddp_timeout`: 1800
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `include_num_input_tokens_seen`: no
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: True
- `use_cache`: False
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: round_robin
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Framework Versions
- Python: 3.12.3
- Sentence Transformers: 5.2.2
- Transformers: 5.0.0
- PyTorch: 2.10.0+cpu
- Accelerate: 1.12.0
- Datasets: 4.5.0
- Tokenizers: 0.22.2

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->